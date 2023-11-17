"use client";
import { FlightCharts } from "@/components/FlightCharts";
import { FlightData } from "@/components/FlightDataTable";
import { FlightsList } from "@/components/FlightsList";
import { PageHeader } from "@/components/PageHeader";
import { fetchInstance } from "@/config/fetch";
import { apiRoutes } from "@/config/routes";
import { RefreshCw } from "lucide-react";
import { useEffect, useState } from "react";
import { BarLoader } from "react-spinners";
import { toast } from "react-toastify";

export interface Flight {
    id: string;
    name: string;
    fileName: string;
    createdAt: string;
    updatedAt: string;
    s3Path: string;
    userId: string;
    predictionResult?: string;
    flightData?: FlightData[];
}

const FlightsPage = () => {
    const [flights, setFlights] = useState<Flight[]>([]);
    const [loading, setLoading] = useState(true);

    const getFlights = async () => {
        setLoading(true)
        try {
            const data = await fetchInstance(apiRoutes.flight.get, {
                cache: "no-cache",
            });
            setFlights(data);
            toast.success("Voos carregados com sucesso.");
        } catch (error) {
            toast.error("Não foi possível carregar os voos.");
        }
        setLoading(false)
    };

    useEffect(() => {
        getFlights();
    }, []);

    return (
        <div className="relative w-full">
            <PageHeader title="Voos" subtitle="Predições do sistema de bleed dos voos" />
            <RefreshCw
                onClick={getFlights}
                className="absolute right-10 top-0 hover:scale-105 transition cursor-pointer"
                size={40}
            />
            {loading ? (
                <BarLoader width={"100%"} color="#00a0e6" />
            ) : (
                <>
                    <FlightCharts flights={flights} />
                    <FlightsList flights={flights} />
                </>
            )}
        </div>
    );
};

export default FlightsPage;
