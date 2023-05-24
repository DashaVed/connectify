export const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000/api';
export const WEBSOCKET_URL = (
    import.meta.env.WEBSOCKET_URL ||
    API_URL.replace("http", "ws").replace("/api", '/ws')
);