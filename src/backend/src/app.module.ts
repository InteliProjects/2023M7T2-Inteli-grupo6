import { Module } from '@nestjs/common';

import { FlightModule } from './flight/flight.module';
import { ConfigModule } from '@nestjs/config';
import { PrismaModule } from './prisma/prisma.module';
import { AuthModule } from './auth/auth.module';
import { UsersModule } from './users/users.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true, }),
    FlightModule,
    AuthModule,
    UsersModule,
    PrismaModule,
  ],
})
export class AppModule { }
