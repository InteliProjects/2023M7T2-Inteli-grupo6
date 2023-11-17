# Utilize a imagem oficial do Node.js como base
FROM node:lts

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

RUN npx prisma generate

RUN npx prisma migrate deploy

RUN npx prisma db pull

RUN npm run build

EXPOSE 3001

CMD ["npm", "run", "start:prod"]