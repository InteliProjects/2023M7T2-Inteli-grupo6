"use client";
import { Flight } from "@/app/protected/flights/page";
import { formatDate } from "@/utils/date";
import React, { use, useState } from "react";
import { FlightDetails } from "../FlightDetails";
import { Card } from "../Card";
import { useRouter } from "next/navigation";
import { routes } from "@/config/routes";

interface FlightsListProps {
    flights: Flight[];
}

export const FlightsList: React.FC<FlightsListProps> = ({ flights }) => {
    const router = useRouter();

    return (
        <>
            {flights.length > 0 ? (
                <div className="grid grid-cols-4 gap-8">
                    {flights.map((flight) => (
                        <div
                            className="cursor-pointer hover:scale-105 transition-all"
                            onClick={() => router.push(routes.flight.data(flight.id))}
                            key={flight.id}
                        >
                            <Card key={flight.id}>
                                <h2 className="text-xl font-medium">{flight.name}</h2>
                                <p className="mt-2">
                                    Status da predição:{" "}
                                    {flight.predictionResult ? (
                                        <span className="text-green-400">Finalizada</span>
                                    ) : (
                                        <span className="text-red-400">Pendente</span>
                                    )}
                                    {flight.predictionResult && (
                                        <p className="mt-6">
                                            Resultado:{" "}
                                            {parseInt(flight.predictionResult) === 0 ? (
                                                <span className="text-green-400">Sem problemas no sistema de bleed</span>
                                            ) : (
                                                <span className="text-red-400">Possível problema no sistema de bleed</span>
                                            )}
                                        </p>
                                    )}
                                </p>

                                <a
                                    href={flight.s3Path}
                                    className="text-primary block mt-6 hover:scale-105 transition-all"
                                >
                                    Baixar detalhes do voo
                                </a>
                                <p className="mt-4">{formatDate(flight.createdAt)}</p>
                            </Card>
                        </div>
                    ))}
                </div>
            ) : (
                <p className="text-xl text-center w-full">Nenhum registro</p>
            )}
        </>
    );
};
