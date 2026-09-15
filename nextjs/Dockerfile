FROM node:24-bookworm-slim

ENV NEXT_TELEMETRY_DISABLED=1
WORKDIR /app

COPY package.json .
RUN npm install --omit=dev && npm cache clean --force

COPY app ./app
RUN npm run build

ENV NODE_ENV=production
USER node
EXPOSE 3000
CMD ["npm", "run", "start", "--", "-H", "0.0.0.0", "-p", "3000"]
