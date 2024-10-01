import React, { useEffect } from "react";
import Navbar from "../components/Navbar";
import Announcement from "../components/Announcement";
import Slider from "../components/Slider";
import Categories from "../components/Categories";
import PopularProducts from "../components/PopularProducts";
import Footer from "../components/Footer";
import { fetchCartData } from "../redux/apiCalls";
import { useDispatch, useSelector } from "react-redux";

const Home = () => {
  const dispatch = useDispatch();
  // const user = useSelector((store) => store.user.currentUser);
  // console.log(user);
  // useEffect(() => {
  //   const fetchCartDataHandler = async () => {
  //     await fetchCartData(dispatch, user);
  //   };
  //   fetchCartDataHandler();
  // }, [user]);

  useEffect(() => {
    const fetchCartDataHandler = async () => {
      await fetchCartData(dispatch);
    };
    fetchCartDataHandler();
  }, []);
  return (
    <div>
      <Announcement />
      <Navbar />
      <Slider />
      <Categories />
      <PopularProducts />
      <Footer />
    </div>
  );
};

export default Home;
