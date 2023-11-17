import {
  Body,
  Controller,
  Get,
  Param,
  Patch,
  Req,
  Request,
  UseGuards,
} from '@nestjs/common';
import { ApiBearerAuth, ApiTags } from '@nestjs/swagger';
import { JwtAuthGuard } from 'src/auth/guards/jwt-auth.guard';
import { UsersService } from './users.service';
import { Roles } from 'src/auth/decorators/roles.decorator';
import { Role } from '@prisma/client';
import { UserEditDto } from './dtos/user-edit';
import { AdminEditDto } from './dtos/admin-edit';

@ApiTags('Users')
@Controller('users')
export class UsersController {
  constructor(private usersService: UsersService) {}

  @Roles(Role.ADMIN)
  @UseGuards(JwtAuthGuard)
  @ApiBearerAuth()
  @Get('all')
  getAllUsers() {
    return this.usersService.getAllUsers();
  }

  @UseGuards(JwtAuthGuard)
  @ApiBearerAuth()
  @Get('profile')
  getProfile(@Request() req) {
    return req.user;
  }

  @ApiBearerAuth()
  @UseGuards(JwtAuthGuard)
  @Patch('edit/me')
  editMe(@Req() req, @Body() body: UserEditDto) {
    return this.usersService.editUser(req.user.id, body);
  }

  @ApiBearerAuth()
  @Roles(Role.ADMIN)
  @UseGuards(JwtAuthGuard)
  @Patch('edit/:id')
  editUser(@Param('id') userId: string, @Body() body: AdminEditDto) {
    return this.usersService.editUser(userId, body);
  }
}
