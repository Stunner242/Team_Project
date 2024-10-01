import styled from "styled-components";
import { categories } from "../dataFile";
import CategoryItem from "./CategoryItem";
import { mobile } from "../responsive";

const CategoryWrapper = styled.div`
  display: flex;
  padding: 20px;
  justify-content: space-between;
  ${mobile({ padding: "0px", flexDirection: "column" })}
`;

const Categories = () => {
  return (
    <CategoryWrapper>
      {categories.map((item) => (
        <CategoryItem item={item} key={item.id} />
      ))}
    </CategoryWrapper>
  );
};

export default Categories;
