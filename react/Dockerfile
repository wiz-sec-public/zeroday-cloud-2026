FROM node:24-bookworm-slim

ENV NODE_ENV=production
WORKDIR /app

COPY package.json .
RUN npm install --omit=dev && npm cache clean --force

COPY server.js .
USER node
EXPOSE 3000
CMD ["npm", "start"]
