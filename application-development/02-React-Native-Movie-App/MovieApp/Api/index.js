const url = "http://www.omdbapi.com/?apikey=393c9d07";

export const fetchMovies = async (title) => {
  try {
    const res = await fetch(`${url}&s=${title}`);
    const data = await res.json();
    return data;
  } catch (error) {
    console.log(error.response);
  }
};
