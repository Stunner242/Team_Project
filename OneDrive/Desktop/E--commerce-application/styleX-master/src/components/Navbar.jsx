import React from "react";
import styled from "styled-components";
import { Badge } from "@mui/material";
import { Search, ShoppingCartOutlined } from "@mui/icons-material";
import { Link, useNavigate } from "react-router-dom";
import { mobile } from "../responsive";
import { useDispatch, useSelector } from "react-redux";
import { emptyCart } from "../redux/cartRedux";
import { logout } from "../redux/userRedux";

const NavContainer = styled.div`
  /* height: 60px; */
  ${mobile({ height: "50px" })}
`;

const Wrapper = styled.div`
  padding: 10px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  ${mobile({ padding: "10px 0px" })}
`;

const Left = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
`;

const Language = styled.span`
  font-size: 14px;
  cursor: pointer;
  ${mobile({ display: "none" })}
`;

const SearchContainer = styled.div`
  border: 0.5px solid lightgray;
  display: flex;
  align-items: center;
  margin-left: 25px;
  padding: 5px;
`;

const Input = styled.input`
  border: none;
  ${mobile({ width: "50px" })}
`;

const Center = styled.div`
  flex: 1;
  text-align: center;
`;

const Logo = styled.h1`
  font-weight: bold;
  cursor: pointer;
  ${mobile({ fontSize: "24px" })}
`;
const Right = styled.div`
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: flex-end;
  ${mobile({ flex: 2, justifyContent: "center" })}
`;

const MenuItem = styled.div`
  font-size: 14px;
  cursor: pointer;
  margin-left: 25px;
  ${mobile({ fontSize: "12px", marginLeft: "10px" })}
`;

const Avatar = styled.div`
  /* padding: 5px; */
  background-image: url("https://www.w3schools.com/howto/img_avatar.png");
  background-repeat: no-repeat;
  background-size: contain;
  background-position: center;
  border-radius: 100%;
`;
const Image = styled.img`
  width: 100%;
  height: 30px;
  border-radius: 100%;
`;

const Navbar = () => {
  const quantity = useSelector((state) => state.cart.quantity);
  const user = useSelector((state) => state.user.currentUser);
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const logoutHandler = () => {
    window.localStorage.clear();
    dispatch(logout());
    dispatch(emptyCart());
    // console.log("Logged out");
  };
  return (
    <NavContainer>
      <Wrapper>
        <Left>
          <Language>EN</Language>
          <SearchContainer>
            <Input placeholder="Search" />
            <Search style={{ color: "gray", fontSize: 16 }} />
          </SearchContainer>
        </Left>
        <Center>
          <Logo
            onClick={() => {
              navigate("/");
            }}
          >
            StyleX
          </Logo>
        </Center>
        {!user && (
          <Right>
            <MenuItem
              onClick={() => {
                navigate("/register");
              }}
            >
              REGISTER
            </MenuItem>
            <MenuItem
              onClick={() => {
                navigate("/login");
              }}
            >
              SIGN IN
            </MenuItem>
            <Link to="/cart">
              <MenuItem>
                <Badge badgeContent={quantity} color="primary">
                  <ShoppingCartOutlined />
                </Badge>
              </MenuItem>
            </Link>
          </Right>
        )}
        {user !== null && (
          <Right>
            <Avatar>
              <Image
                src="https://www.w3schools.com/howto/img_avatar.png"
                alt="avatar"
              ></Image>
            </Avatar>
            <MenuItem onClick={logoutHandler}>LOGOUT</MenuItem>
            <Link to="/cart">
              <MenuItem>
                <Badge badgeContent={quantity} color="primary">
                  <ShoppingCartOutlined />
                </Badge>
              </MenuItem>
            </Link>
          </Right>
        )}
      </Wrapper>
    </NavContainer>
  );
};

export default Navbar;
