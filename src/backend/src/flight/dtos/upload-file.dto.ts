import { ApiProperty } from '@nestjs/swagger';

export class UploadFileDto {
  @ApiProperty({
    description: 'Nome do arquivo',
    type: 'string',
  })
  name: string;

  @ApiProperty({
    description: 'Arquivo para upload',
    type: 'string',
    format: 'binary',
  })
  file: Express.Multer.File;
}