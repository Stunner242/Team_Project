import { useEffect, useState } from "react";
// import { useDispatch } from "react-redux";
import { useLocation } from "react-router-dom";
import { Add, Remove } from "@mui/icons-material";
import styled from "styled-components";
import Announcement from "../components/Announcement";
import Footer from "../components/Footer";
import Navbar from "../components/Navbar";
// import Newsletter from "../components/Newsletter";
import { publicRequest } from "../requestMethods";
import { useDispatch, useSelector } from "react-redux";
import { mobile } from "../responsive";
import { addToCart, fetchCartData } from "../redux/apiCalls";

const Container = styled.div``;

const Wrapper = styled.div`
  padding: 50px;
  display: flex;
  ${mobile({ padding: "10px", flexDirection: "column" })}
`;
const LoadingWrapper = styled.div`
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 70vh;
`;

const ImgContainer = styled.div`
  flex: 1;
`;

const Image = styled.img`
  width: 100%;
  height: 90vh;
  object-fit: cover;
  ${mobile({ height: "40vh" })}
`;

const InfoContainer = styled.div`
  flex: 1;
  padding: 0px 50px;
  ${mobile({ padding: "10px" })}
`;

const Title = styled.h1`
  font-weight: 200;
`;

const Desc = styled.p`
  margin: 20px 0px;
`;

const Price = styled.span`
  font-weight: 100;
  font-size: 40px;
`;

const FilterContainer = styled.div`
  width: 50%;
  margin: 30px 0px;
  display: flex;
  justify-content: space-between;
  ${mobile({ width: "100%" })}
`;

const Filter = styled.div`
  display: flex;
  align-items: center;
`;

const FilterTitle = styled.span`
  font-size: 20px;
  font-weight: 200;
`;

const FilterColor = styled.div`
  width: 20px;
  height: 20px;
  border-radius: 50%;
  background-color: ${(props) => props.color};
  margin: 0px 5px;
  cursor: pointer;
`;

const FilterSize = styled.select`
  margin-left: 10px;
  padding: 5px;
`;

const FilterSizeOption = styled.option``;

const AddContainer = styled.div`
  width: 50%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  ${mobile({ width: "100%" })}
`;

const AmountContainer = styled.div`
  display: flex;
  align-items: center;
  font-weight: 700;
`;

const Amount = styled.span`
  width: 30px;
  height: 30px;
  border-radius: 10px;
  border: 1px solid pink;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0px 5px;
`;

const Button = styled.button`
  padding: 15px;
  border: 2px solid pink;
  background-color: white;
  cursor: pointer;
  color: black;
  font-weight: 500;
  &:hover {
    background-color: #f8f4f4;
  }
`;
const DummyButton = styled.div`
  padding: 15px;
  border: 2px solid black;
  background-color: gray;
  cursor: not-allowed;
  font-weight: 500;
`;

const Product = () => {
  const location = useLocation();
  const id = location.pathname.split("/")[2];
  const [product, setProduct] = useState({
    id: 1,
    img: "https://img.fruugo.com/product/7/25/359425257_max.jpg",
    title: "SUMMER SALE",
    desc: "DON'T COMPROMISE ON STYLE! GET FLAT 30% OFF FOR NEW ARRIVALS.",
    price: 1000,
  });
  const [quantity, setQuantity] = useState(1);
  const [color, setColor] = useState("");
  const [size, setSize] = useState("");
  const dispatch = useDispatch();
  const user = useSelector((store) => store.user);
  const cart = useSelector((store) => store.cart);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const getProduct = async () => {
      setLoading(true);
      try {
        const res = await publicRequest.get("/products/find/" + id);
        setProduct(res.data);
        setLoading(false);
      } catch (err) {
        setLoading(false);
      }
    };
    getProduct();
  }, [id]);

  useEffect(() => {}, []);
  const handleQuantity = (type) => {
    if (type === "dec") {
      quantity > 1 && setQuantity(quantity - 1);
    } else {
      setQuantity(quantity + 1);
    }
  };

  const handleClick = async () => {
    try {
      await addToCart(dispatch, product._id, quantity, color, size);
      // await fetchCartData(dispatch, user.currentUser);
      await fetchCartData(dispatch);
    } catch (error) {
      console.log(error);
    }
  };
  return (
    <Container>
      <Navbar />
      <Announcement />
      {loading ? (
        <LoadingWrapper>Loading...</LoadingWrapper>
      ) : (
        <Wrapper>
          <ImgContainer>
            <Image src={product.img} alt="product" />
          </ImgContainer>
          <InfoContainer>
            <Title>{product.title}</Title>
            <Desc>{product.desc}</Desc>
            <Price>Rs. {product.price}</Price>
            <FilterContainer>
              <Filter>
                <FilterTitle>Color</FilterTitle>
                {product.color?.map((c) => (
                  <FilterColor color={c} key={c} onClick={() => setColor(c)} />
                ))}
              </Filter>
              <Filter>
                <FilterTitle>Size</FilterTitle>
                <FilterSize onChange={(e) => setSize(e.target.value)}>
                  {product.size?.map((s) => (
                    <FilterSizeOption key={s}>{s}</FilterSizeOption>
                  ))}
                </FilterSize>
              </Filter>
            </FilterContainer>
            <AddContainer>
              <AmountContainer>
                <Remove onClick={() => handleQuantity("dec")} />
                <Amount>{quantity}</Amount>
                <Add onClick={() => handleQuantity("inc")} />
              </AmountContainer>
              {user.currentUser ? (
                <Button onClick={handleClick}>
                  {cart.isFetching ? "Loading..." : "ADD TO CART"}
                </Button>
              ) : (
                <DummyButton>Login to add to cart!</DummyButton>
              )}
            </AddContainer>
          </InfoContainer>
        </Wrapper>
      )}
      <Footer />
    </Container>
  );
};

export default Product;
