"use client";
import { MRT_ColumnDef, MaterialReactTable } from "material-react-table";
import React, { useMemo } from "react";

export interface FlightData {
    id: string;
    aircraftSerNum1: number;
    amscChBasHealthStatus1: number;
    amscChBasHealthStatus2: number;
    amscHprsovDrivF1: number;
    amscHprsovDrivF2: number;
    amscPrsovDrivF1: number;
    amscPrsovDrivF2: number;
    basBleedLowPressF1: number;
    basBleedLowPressF2: number;
    basBleedLowTempF1: number;
    basBleedLowTempF2: number;
    basBleedOverPressF1: number;
    basBleedOverPressF2: number;
    basBleedOverTempF1: number;
    basBleedOverTempF2: number;
    bleedAcsBleedConfigStatus1: number;
    bleedAcsBleedConfigStatus2: number;
    bleedFavTmCmd1: number;
    bleedFavTmCmd2: number;
    bleedFavTmFbk1: number;
    bleedFavTmFbk2: number;
    bleedHprsovCmdStatus1: number;
    bleedHprsovCmdStatus2: number;
    bleedHprsovOpPosStatus1: number;
    bleedHprsovOpPosStatus2: number;
    bleedMonPress1: number;
    bleedMonPress2: number;
    bleedOnStatus1: number;
    bleedOnStatus2: number;
    bleedOutTemp1: number;
    bleedOutTemp2: number;
    bleedOutTempTarget1: number;
    bleedOutTempTarget2: number;
    bleedOverpressCas1: number;
    bleedOverpressCas2: number;
    bleedPrecoolDiffPress1: number;
    bleedPrecoolDiffPress2: number;
    bleedPrsovClPosStatus1: number;
    bleedPrsovClPosStatus2: number;
    bleedPrsovFbk1: number;
    bleedPrsovFbk2: number;
    bleedPrsovOpPosStatus1: number;
    bleedPrsovOpPosStatus2: number;
    bleedPrsovTmCmd1: number;
    bleedPrsovTmCmd2: number;
    bleedSingleOperation1: number;
    bleedSingleOperation2: number;
    bleedSwPress1: number;
    bleedSwPress2: number;
    correctedCoreSpeed1a: number;
    correctedCoreSpeed3a: number;
    correctedN1Speed1a: number;
    correctedN1Speed3a: number;
    message0418DAA1: number;
    message0422DAA1: number;
    messageInhibitPhases1: number;
    phaseOfFlight1: number;
    phaseOfFlightNavigation1: number;
    sfyBasFaultWord1Bit131: number;
    sfyBasFaultWord1Bit132: number;
    pressAltitude1: number;
    pressAltitude2: number;
    pressAltitude3: number;
    pressAltitude4: number;
    wOW1: number;
    wOW3: number;
    createdAt: Date;
    flightFileId?: string;
}

interface FlightDataTableProps {
    flightData: FlightData[];
}

export const FlightDataTable: React.FC<FlightDataTableProps> = ({ flightData }) => {
    const columns = useMemo<MRT_ColumnDef<FlightData>[]>(
        () => [
            { accessorKey: "id", header: "ID" },
            { accessorKey: "aircraftSerNum1", header: "Aircraft Serial Number 1" },
            { accessorKey: "amscChBasHealthStatus1", header: "AMSC CH Bas Health Status 1" },
            { accessorKey: "amscChBasHealthStatus2", header: "AMSC CH Bas Health Status 2" },
            { accessorKey: "amscHprsovDrivF1", header: "AMSC HPRSOV Driv F1" },
            { accessorKey: "amscHprsovDrivF2", header: "AMSC HPRSOV Driv F2" },
            { accessorKey: "amscPrsovDrivF1", header: "AMSC PRSOV Driv F1" },
            { accessorKey: "amscPrsovDrivF2", header: "AMSC PRSOV Driv F2" },
            { accessorKey: "basBleedLowPressF1", header: "Bas Bleed Low Press F1" },
            { accessorKey: "basBleedLowPressF2", header: "Bas Bleed Low Press F2" },
            { accessorKey: "basBleedLowTempF1", header: "Bas Bleed Low Temp F1" },
            { accessorKey: "basBleedLowTempF2", header: "Bas Bleed Low Temp F2" },
            { accessorKey: "basBleedOverPressF1", header: "Bas Bleed Over Press F1" },
            { accessorKey: "basBleedOverPressF2", header: "Bas Bleed Over Press F2" },
            { accessorKey: "basBleedOverTempF1", header: "Bas Bleed Over Temp F1" },
            { accessorKey: "basBleedOverTempF2", header: "Bas Bleed Over Temp F2" },
            { accessorKey: "bleedAcsBleedConfigStatus1", header: "Bleed ACS Bleed Config Status 1" },
            { accessorKey: "bleedAcsBleedConfigStatus2", header: "Bleed ACS Bleed Config Status 2" },
            { accessorKey: "pressAltitude4", header: "Press Altitude 4" },
            { accessorKey: "wOW1", header: "WOW 1" },
            { accessorKey: "wOW3", header: "WOW 3" },
            { accessorKey: "createdAt", header: "Created At" },
            { accessorKey: "flightFileId", header: "Flight File ID" },
        ],
        []
    );

    return (
            <MaterialReactTable
                columns={columns}
                data={flightData}
                enableRowSelection={false}
                enableSelectAll={false}
                enableGlobalFilter={true}
            />
    );
};
