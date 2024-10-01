import styled from "styled-components";

const FooterWrapper = styled.div`
  height: 20vh;
  background-color: #fcf5f5;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-direction: column;
`;

const Desc = styled.div`
  font-size: 20px;
  font-weight: 300;
`;

const Footer = () => {
  return (
    <FooterWrapper>
      {/* <Desc>
        Made With ❤️ by{" "}
        <a
          href="https://nitya-singh.netlify.app"
          target="_blank"
          rel="noreferrer noopener"
        >
          Nitya Singh
        </a>{" "}
      </Desc> */}
    </FooterWrapper>
  );
};

export default Footer;
