import redis from 'redis';

// Create redis client instance
const client = redis.createClient()

// Event listener for successful connection
client.on("connect", () => {
	console.log("Redis client connected to the server");
});

// Event listener for connection error
client.on('error', (error) => {
	console.log(`Redis client not connected to the server: ${error}`)
});

// close the redis client connection
client.quit()
