import { Injectable } from '@nestjs/common';
import { PrismaService } from '../prisma/prisma.service';

@Injectable()
export class FlightService {
  constructor(private prisma: PrismaService) {}

  async getFlights() {
    return await this.prisma.flightFile.findMany({
      orderBy: {
        createdAt: 'desc',
      },
      include: {
        user: true,
      },
    });
  }

  async getFlight(id: string) {
    return await this.prisma.flightFile.findUnique({
      where: {
        id,
      },
      include: {
        flightData: true,
      },
    });
  }

  async createFlightFile(data) {
    return await this.prisma.flightFile.create({
      data,
    });
  }
}
