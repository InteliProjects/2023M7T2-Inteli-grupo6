//files.controller.ts
import {
  BadRequestException,
  Body,
  Controller,
  Get,
  Post,
  Request,
  UploadedFile,
  UseGuards,
  UseInterceptors,
} from '@nestjs/common';
import { FileInterceptor } from '@nestjs/platform-express';
import { ApiBearerAuth, ApiBody, ApiConsumes, ApiTags } from '@nestjs/swagger';
import { JwtAuthGuard } from 'src/auth/guards/jwt-auth.guard';
import multerConfig from './multer-config';
import { FlightService } from './flight.service';

@ApiTags('Flight')
@Controller('flight')
export class FlightController {
  constructor(private readonly flightService: FlightService) {}

  @UseGuards(JwtAuthGuard)
  @Get()
  @ApiBearerAuth()
  async getFlights() {
    const flights = await this.flightService.getFlights();
    return flights;
  }

  @UseGuards(JwtAuthGuard)
  @Get(':id')
  @ApiBearerAuth()
  async getFlight(@Request() req) {
    const flight = await this.flightService.getFlight(req.params.id);
    return flight;
  }

  @UseGuards(JwtAuthGuard)
  @Post('create')
  @UseInterceptors(FileInterceptor('file', multerConfig))
  @ApiConsumes('multipart/form-data')
  @ApiBearerAuth()
  @ApiBody({
    description: 'Upload de arquivo parquet',
    type: 'multipart/form-data',
    required: true,
    schema: {
      type: 'object',
      properties: {
        file: {
          type: 'string',
          format: 'binary',
        },
        name: {
          type: 'string',
        },
      },
    },
  })
  async uploadArquivo(@Body() body, @Request() req, @UploadedFile() file) {
    if (!file) throw new BadRequestException('Erro no upload do arquivo.');

    // Após o upload bem-sucedido para o S3, crie um registro na tabela flighFile
    const flighFile = {
      userId: req.user.id,
      name: body.name,
      fileName: file.key,
      s3Path: file.location,
    };

    const savedFile = await this.flightService.createFlightFile(flighFile);

    return savedFile;
  }
}
