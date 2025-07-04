#stage1: build the application
#use image Node.js to build nad run React
FROM node:20-alpine AS build

#working foler in container
WORKDIR /app

#copy json package
COPY package.json .
# install React
RUN npm install

COPY . .

RUN npm run build

#stage2: run the application

FROM node:20-alpine 

WORKDIR /app

#set production enviroment
ENV NODE_ENV production

#copy build files from build stage
COPY --from=build /app/build .

#copy necessary files
COPY --from=build /app/package.json .

#set files permission

RUN chown -R node:node /app
USER node
#install production dependencies
RUN npm install --omit=dev
# open port 3000 for dev React
EXPOSE 3000
#Command run React app
CMD ["npm", "start"]

