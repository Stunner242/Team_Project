import { createSlice } from "@reduxjs/toolkit";

const cartSlice = createSlice({
  name: "cart",
  initialState: {
    cartProducts: [],
    quantity: 0,
    total: 0,
  },
  reducers: {
    populateCart: (state, action) => {
      state.cartProducts = action.payload;
      state.quantity = action.payload.length;
      state.total = action.payload.reduce((total, product) => {
        return total + product.quantity * product.details.price;
      }, 0);
    },
    emptyCart: (state, action) => {
      state.quantity = 0;
      state.cartProducts = [];
      state.total = 0;
    },
  },
});

export const { populateCart, emptyCart } = cartSlice.actions;
export default cartSlice.reducer;
