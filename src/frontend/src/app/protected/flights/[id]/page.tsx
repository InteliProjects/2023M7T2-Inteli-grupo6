import { FlightDetails } from "@/components/FlightDetails";
import { PageHeader } from "@/components/PageHeader";
import React from "react";

const FlightDetailsPage = () => {
    return (
        <>
            <PageHeader title="Voos" subtitle="Predições do sistema de bleed dos voos" />
            <FlightDetails />
        </>
    );
};

export default FlightDetailsPage;
