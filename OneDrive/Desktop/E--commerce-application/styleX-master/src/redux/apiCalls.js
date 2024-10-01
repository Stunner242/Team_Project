import { loginFailure, loginStart, loginSuccess } from "./userRedux";
import { publicRequest, userRequest } from "../requestMethods";
import { populateCart } from "./cartRedux";
import axios from "axios";

export const login = async (dispatch, user) => {
  dispatch(loginStart());
  try {
    const res = await publicRequest.post("/auth/login", user);
    // console.log(res);
    dispatch(loginSuccess(res.data));
  } catch (err) {
    dispatch(loginFailure());
  }
};

export const addToCart = async (dispatch, productID, quantity, color, size) => {
  try {
    const user = JSON.parse(localStorage.getItem("persist:root"))?.user;
    const currentUser = user && JSON.parse(user).currentUser;
    const token = currentUser?.accessToken;
    const config = {
      headers: {
        token: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    };
    const data = { productID, quantity, color, size };
    const res = await userRequest.post("/cart/add", data, config);
    // console.log(res);
  } catch (error) {
    console.log(error);
  }
};

export const fetchCartData = async (dispatch) => {
  try {
    const user = JSON.parse(localStorage.getItem("persist:root"))?.user;
    const currentUser = user && JSON.parse(user).currentUser;
    const token = currentUser?.accessToken;
    const config = {
      headers: {
        token: `Bearer ${token}`,
      },
    };
    const res = await userRequest.get(`/cart/find/${currentUser._id}`, config);
    // console.log(res.data);
    dispatch(populateCart(res.data));
  } catch (err) {
    console.log(err);
  }
};
