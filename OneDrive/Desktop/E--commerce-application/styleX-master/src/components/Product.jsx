import styled from "styled-components";
import {
  ShoppingCartOutlined,
  FavoriteBorderOutlined,
  SearchOutlined,
} from "@mui/icons-material";
import { Link } from "react-router-dom";

const Explore = styled.div`
  opacity: 0;
  width: 100%;
  height: 100%;
  position: absolute;
  top: 0;
  left: 0;
  background-color: rgba(0, 0, 0, 0.2);
  z-index: 3;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.5s ease;
  cursor: pointer;
`;

const ProductWrapper = styled.div`
  flex: 1;
  margin: 5px;
  min-width: 400px;
  height: 350px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f5fbfd;
  position: relative;

  &:hover ${Explore} {
    opacity: 1;
  }
`;
const Circle = styled.div`
  width: 200px;
  height: 200px;
  border-radius: 50%;
  background-color: white;
  position: absolute;
`;

const PopularProductImage = styled.img`
  height: 100%;
  z-index: 2;
  width: 50%;
  object-fit: cover;
`;

const Icon = styled.div`
  width: 40px;
  height: 40px;
  border-radius: 50%;
  background-color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 10px;
  transition: all 0.5s ease;
  &:hover {
    background-color: #e9f5f5;
    transform: scale(1.1);
  }
`;

const Product = ({ item }) => {
  return (
    <ProductWrapper>
      {/* <Circle /> */}
      <PopularProductImage src={item.img} />
      <Explore>
        <Icon>
          <Link to={`/product/${item._id}`}>
            <SearchOutlined />
          </Link>
        </Icon>
        <Icon>
          <FavoriteBorderOutlined />
        </Icon>
        <Icon>
          <ShoppingCartOutlined />
        </Icon>
      </Explore>
    </ProductWrapper>
  );
};

export default Product;
