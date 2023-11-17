export const routes = {
  flight: {
    base: '/protected/flights',
    create: '/protected/flights/create',
    data: (id: string) => `/protected/flights/${id}`,
  },
  auth: {
    login: "/auth/login"
  },
  admin: {
    users: '/protected/admin/users',
  }
}

export const apiRoutes = {
  auth: {
    login: '/api/auth/login',
    signup: '/api/auth/signup',
  },
  admin: {
    usersAll: '/api/users/all',
    userEdit: (id: string) => `/api/users/edit/${id}`,
  },
  flight: {
    get: '/api/flight',
    create: '/api/flight/create',
    getFlight: (id:string) => `/api/flight/${id}`
  }
}