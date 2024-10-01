import styled from "styled-components";

const AnnouncementWrapper = styled.div`
height: 30px;
  background-color: pink;
  color: white;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  font-weight: 500;
`;

const Announcement = () => {
  return (
    <AnnouncementWrapper>
      StyleX Big Trillion Days. Super Deal! Free Shipping on orders above Rs.
      500
    </AnnouncementWrapper>
  );
};

export default Announcement;
