import redis from "redis";
import { promisify } from "util";

const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on("connect", () => {
  console.log("Redis client connected to the server");
});

client.on("error", (err) => {
  console.log(`Redis client not connected to the server: ${err.message}`);
});

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schooleName) {
  try {
    const value = await getAsync(schooleName);
    console.log(value);
  } catch (err) {
    console.log(err.message);
  }
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");

export default client;
