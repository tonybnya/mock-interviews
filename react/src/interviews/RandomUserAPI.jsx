import { useEffect, useState } from "react";
import axios from "axios";
import UserCard from "../components/UserCard";
import Spinner from "../components/Spinner";

const RandomUserAPI = () => {
  const [user, setUser] = useState({});
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(false);

  const fetchUser = async () => {
    setLoading(true);
    setError(false);
    try {
      const response = await axios.get("https://randomuser.me/api");
      setUser(response.data);
    } catch (err) {
      console.error(err.message);
      setError(true);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchUser();
  }, []);

  return (
    <div className="min-h-screen flex flex-col items-center justify-center px-4">
      {loading && <Spinner />}

      {error && (
        <p className="text-red-500 font-semibold text-xl">
          Something went wrong. Please try again.
        </p>
      )}

      {!loading && !error && user.results && (
        <UserCard
          firstName={user.results[0].name.first}
          lastName={user.results[0].name.last}
          email={user.results[0].email}
          phone={user.results[0].phone}
          city={user.results[0].location.city}
          state={user.results[0].location.state}
          country={user.results[0].location.country}
          dob={new Date(user.results[0].dob.date).toLocaleDateString()}
          age={user.results[0].dob.age}
          profile={user.results[0].picture.medium}
        />
      )}

      <button
        onClick={fetchUser}
        className="mt-6 py-3 px-6 rounded-md font-bold cursor-pointer bg-green-700 hover:bg-green-800 text-white transition"
      >
        Get New User
      </button>
    </div>
  );
};

export default RandomUserAPI;
