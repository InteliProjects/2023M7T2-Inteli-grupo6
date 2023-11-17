-- CreateEnum
CREATE TYPE "Role" AS ENUM ('USER', 'ADMIN');

-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "password" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "roles" "Role"[] DEFAULT ARRAY['USER']::"Role"[],
    "approved" BOOLEAN NOT NULL DEFAULT false,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "FlightFile" (
    "id" TEXT NOT NULL,
    "name" TEXT NOT NULL,
    "fileName" TEXT NOT NULL,
    "s3Path" TEXT NOT NULL,
    "userId" TEXT NOT NULL,
    "predictionResult" TEXT,
    "createdAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "FlightFile_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "FlightData" (
    "id" TEXT NOT NULL,
    "aircraftSerNum1" INTEGER NOT NULL,
    "amscChBasHealthStatus1" DECIMAL(40,20) NOT NULL,
    "amscChBasHealthStatus2" DECIMAL(40,20) NOT NULL,
    "amscHprsovDrivF1" DECIMAL(40,20) NOT NULL,
    "amscHprsovDrivF2" DECIMAL(40,20) NOT NULL,
    "amscPrsovDrivF1" DECIMAL(40,20) NOT NULL,
    "amscPrsovDrivF2" DECIMAL(40,20) NOT NULL,
    "basBleedLowPressF1" DECIMAL(40,20) NOT NULL,
    "basBleedLowPressF2" DECIMAL(40,20) NOT NULL,
    "basBleedLowTempF1" DECIMAL(40,20) NOT NULL,
    "basBleedLowTempF2" DECIMAL(40,20) NOT NULL,
    "basBleedOverPressF1" DECIMAL(40,20) NOT NULL,
    "basBleedOverPressF2" DECIMAL(40,20) NOT NULL,
    "basBleedOverTempF1" DECIMAL(40,20) NOT NULL,
    "basBleedOverTempF2" DECIMAL(40,20) NOT NULL,
    "bleedAcsBleedConfigStatus1" DECIMAL(40,20) NOT NULL,
    "bleedAcsBleedConfigStatus2" DECIMAL(40,20) NOT NULL,
    "bleedFavTmCmd1" DECIMAL(40,20) NOT NULL,
    "bleedFavTmCmd2" DECIMAL(40,20) NOT NULL,
    "bleedFavTmFbk1" DECIMAL(40,20) NOT NULL,
    "bleedFavTmFbk2" DECIMAL(40,20) NOT NULL,
    "bleedHprsovCmdStatus1" DECIMAL(40,20) NOT NULL,
    "bleedHprsovCmdStatus2" DECIMAL(40,20) NOT NULL,
    "bleedHprsovOpPosStatus1" DECIMAL(40,20) NOT NULL,
    "bleedHprsovOpPosStatus2" DECIMAL(40,20) NOT NULL,
    "bleedMonPress1" DECIMAL(40,20) NOT NULL,
    "bleedMonPress2" DECIMAL(40,20) NOT NULL,
    "bleedOnStatus1" DECIMAL(40,20) NOT NULL,
    "bleedOnStatus2" DECIMAL(40,20) NOT NULL,
    "bleedOutTemp1" DECIMAL(40,20) NOT NULL,
    "bleedOutTemp2" DECIMAL(40,20) NOT NULL,
    "bleedOutTempTarget1" DECIMAL(40,20) NOT NULL,
    "bleedOutTempTarget2" DECIMAL(40,20) NOT NULL,
    "bleedOverpressCas1" DECIMAL(40,20) NOT NULL,
    "bleedOverpressCas2" DECIMAL(40,20) NOT NULL,
    "bleedPrecoolDiffPress1" DECIMAL(40,20) NOT NULL,
    "bleedPrecoolDiffPress2" DECIMAL(40,20) NOT NULL,
    "bleedPrsovClPosStatus1" DECIMAL(40,20) NOT NULL,
    "bleedPrsovClPosStatus2" DECIMAL(40,20) NOT NULL,
    "bleedPrsovFbk1" DECIMAL(40,20) NOT NULL,
    "bleedPrsovFbk2" DECIMAL(40,20) NOT NULL,
    "bleedPrsovOpPosStatus1" DECIMAL(40,20) NOT NULL,
    "bleedPrsovOpPosStatus2" DECIMAL(40,20) NOT NULL,
    "bleedPrsovTmCmd1" DECIMAL(40,20) NOT NULL,
    "bleedPrsovTmCmd2" DECIMAL(40,20) NOT NULL,
    "bleedSingleOperation1" DECIMAL(40,20) NOT NULL,
    "bleedSingleOperation2" DECIMAL(40,20) NOT NULL,
    "bleedSwPress1" DECIMAL(40,20) NOT NULL,
    "bleedSwPress2" DECIMAL(40,20) NOT NULL,
    "correctedCoreSpeed1a" DECIMAL(40,20) NOT NULL,
    "correctedCoreSpeed3a" DECIMAL(40,20) NOT NULL,
    "correctedN1Speed1a" DECIMAL(40,20) NOT NULL,
    "correctedN1Speed3a" DECIMAL(40,20) NOT NULL,
    "message0418DAA1" DOUBLE PRECISION NOT NULL,
    "message0422DAA1" DOUBLE PRECISION NOT NULL,
    "messageInhibitPhases1" DECIMAL(40,20) NOT NULL,
    "phaseOfFlight1" DECIMAL(40,20) NOT NULL,
    "phaseOfFlightNavigation1" DECIMAL(40,20) NOT NULL,
    "sfyBasFaultWord1Bit131" DECIMAL(40,20) NOT NULL,
    "sfyBasFaultWord1Bit132" DECIMAL(40,20) NOT NULL,
    "pressAltitude1" DECIMAL(40,20) NOT NULL,
    "pressAltitude2" DECIMAL(40,20) NOT NULL,
    "pressAltitude3" DECIMAL(40,20) NOT NULL,
    "pressAltitude4" DECIMAL(40,20) NOT NULL,
    "wOW1" DECIMAL(40,20) NOT NULL,
    "wOW3" DECIMAL(40,20) NOT NULL,
    "createdAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "flightFileId" TEXT,

    CONSTRAINT "FlightData_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Predicted" (
    "id" TEXT NOT NULL,
    "output" TEXT NOT NULL,
    "flightFileId" TEXT NOT NULL,
    "createdAt" TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Predicted_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_email_key" ON "User"("email");

-- AddForeignKey
ALTER TABLE "FlightFile" ADD CONSTRAINT "FlightFile_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "FlightData" ADD CONSTRAINT "FlightData_flightFileId_fkey" FOREIGN KEY ("flightFileId") REFERENCES "FlightFile"("id") ON DELETE SET NULL ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "Predicted" ADD CONSTRAINT "Predicted_flightFileId_fkey" FOREIGN KEY ("flightFileId") REFERENCES "FlightFile"("id") ON DELETE RESTRICT ON UPDATE CASCADE;
