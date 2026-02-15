# myip

A minimal Docker container that returns the caller's IP address as plain text.

## Build

```bash
docker build -t myip .
```

## Run

```bash
docker run -d -p 8080:8080 myip
```

## Usage

```bash
curl http://localhost:8080
```

Returns your IP address as plain text.

When behind a reverse proxy, the service reads `X-Forwarded-For` or `X-Real-IP` headers to determine the real client IP.


