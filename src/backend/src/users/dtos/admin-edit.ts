import { ApiProperty } from '@nestjs/swagger';
import { Role } from '@prisma/client';
import { IsOptional } from 'class-validator';

export class AdminEditDto {
  @ApiProperty()
  @IsOptional()
  roles: Role[];

  @ApiProperty()
  @IsOptional()
  approved: boolean;
}
