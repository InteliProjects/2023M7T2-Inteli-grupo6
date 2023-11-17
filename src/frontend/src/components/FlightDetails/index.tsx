"use client";
import { Flight } from "@/app/protected/flights/page";
import Modal from "@/components/Modal";
import { fetchInstance } from "@/config/fetch";
import { apiRoutes } from "@/config/routes";
import { formatDate } from "@/utils/date";
import React, { useEffect, useState } from "react";
import { BarLoader } from "react-spinners";
import { toast } from "react-toastify";
import { FlightDataTable } from "../FlightDataTable";
import { useParams } from "next/navigation";
import { Card } from "../Card";

export const FlightDetails: React.FC = () => {
    const [loading, setLoading] = useState(false);
    const [flightDetails, setFlightDetails] = useState<Flight | null>(null);
    const params = useParams();

    const getFlightDetails = async () => {
        setLoading(true);

        try {
            const res = await fetchInstance(apiRoutes.flight.getFlight(params.id as string));

            setFlightDetails(res);
            setLoading(false);
        } catch (error) {
            toast.error("Erro ao carregar detalhes do voo");
        }
    };

    useEffect(() => {
        getFlightDetails();
    }, []);

    return (
        <>
            {loading ? (
                <BarLoader width={"100%"} color="#00a0e6" />
            ) : (
                flightDetails && (
                    <Card>
                        <h2 className="text-xl font-medium">{flightDetails.name}</h2>
                        <p className="mt-2">
                            Predição:{" "}
                            {flightDetails.predictionResult ? (
                                <span className="text-green-400">Pendente</span>
                            ) : (
                                <span className="text-red-400">Pendente</span>
                            )}
                        </p>

                        <a href={flightDetails.s3Path} className="text-primary block hover:scale-105 transition-all">
                            Baixar detalhes do voo
                        </a>
                        <p className="mt-4">{formatDate(flightDetails.createdAt)}</p>

                        <div className="my-4 w-[74vw] overflow-x-auto">
                            {flightDetails.flightData && <FlightDataTable flightData={flightDetails.flightData} />}
                        </div>
                    </Card>
                )
            )}
        </>
    );
};
