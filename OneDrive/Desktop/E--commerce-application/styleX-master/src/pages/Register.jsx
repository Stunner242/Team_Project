import styled from "styled-components";
import { mobile } from "../responsive";
import { useState } from "react";
import { publicRequest } from "../requestMethods";
import { useNavigate } from "react-router";
import { toast } from "react-toastify";

const Container = styled.div`
  width: 100vw;
  height: 100vh;
  background: linear-gradient(
      rgba(255, 255, 255, 0.5),
      rgba(255, 255, 255, 0.5)
    ),
    url("https://c1.wallpaperflare.com/preview/259/824/859/indian-traditional-colorful-fashion-culture.jpg")
      center;
  background-size: cover;
  display: flex;
  align-items: center;
  justify-content: center;
`;

const Wrapper = styled.div`
  width: 40%;
  padding: 20px;
  background-color: white;
  ${mobile({ width: "75%" })}
`;

const Title = styled.h1`
  font-size: 24px;
  font-weight: 300;
`;

const Form = styled.form`
  display: flex;
  flex-wrap: wrap;
`;

const Input = styled.input`
  flex: 1;
  min-width: 40%;
  margin: 20px 10px 0px 0px;
  padding: 10px;
`;

const Agreement = styled.span`
  font-size: 12px;
  margin: 20px 0px 10px;
`;

const Button = styled.button`
  width: 40%;
  border: none;
  padding: 15px 20px;
  background-color: ${(props) => (props.isActive === true ? "red" : "pink")};
  cursor: ${(props) => (props.isActive === true ? "pointer" : "not-allowed")};
  color: white;
`;

const Link = styled.div`
  margin: 5px 0px;
  font-size: 12px;
  text-decoration: underline;
  cursor: pointer;
  width: 100%;
`;

const Register = () => {
  const [firstName, setFirstname] = useState("");
  const [lastName, setLastname] = useState("");
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [err, setErr] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleValidation = (event) => {
    // const passwordInputValue = event.target.value.trim();
    const passwordInputFieldName = event.target.name;
    if (
      passwordInputFieldName === "confirmPassword" ||
      (passwordInputFieldName === "password" && confirmPassword.length > 0)
    ) {
      if (confirmPassword !== password) {
        setErr("Confirm password does not match");
      } else {
        setErr("");
      }
    }
  };
  const registerHandler = async (e) => {
    e.preventDefault();
    setLoading(true);
    const user = {
      username: username,
      email: email,
      password: password,
      isAdmin: false,
    };
    try {
      await publicRequest.post("/auth/register", user);
      toast.success("Registered Successfully!");
      setLoading(false);
      navigate("/login");
    } catch (error) {
      toast.error(error.response.data);
      setLoading(false);
    }
  };
  const errorCheck = () => {
    if (
      username.trim().length === 0 ||
      firstName.trim().length === 0 ||
      password.trim().length === 0
    ) {
      setErr("All input fields are required.");
      return true;
    } else {
      return false;
    }
  };
  return (
    <Container>
      <Wrapper>
        <Title>CREATE AN ACCOUNT</Title>
        <Form>
          <Input
            required
            type="text"
            value={firstName}
            placeholder="first name"
            onChange={(event) => {
              setFirstname(event.target.value);
            }}
          />
          <Input
            required
            type="text"
            value={lastName}
            placeholder="last name"
            onChange={(event) => {
              setLastname(event.target.value);
            }}
          />
          <Input
            required
            type="text"
            value={username}
            placeholder="username"
            onChange={(event) => {
              setUsername(event.target.value);
            }}
          />
          <Input
            required
            type="email"
            value={email}
            placeholder="email"
            onChange={(event) => {
              setEmail(event.target.value);
            }}
          />
          <Input
            required
            type="password"
            name="password"
            value={password}
            placeholder="password"
            onKeyUp={handleValidation}
            onChange={(event) => {
              setPassword(event.target.value);
            }}
          />
          <Input
            required
            type="password"
            name="confirmPassword"
            value={confirmPassword}
            placeholder="confirm password"
            onKeyUp={handleValidation}
            onChange={(event) => {
              setConfirmPassword(event.target.value);
            }}
          />
          {err}

          <Agreement>
            By creating an account, I consent to the processing of my personal
            data in accordance with the <b>PRIVACY POLICY</b>
          </Agreement>
          <Link
            onClick={() => {
              navigate("/login");
            }}
          >
            EXISTING USER? LOGIN!
          </Link>
          <Button
            onClick={registerHandler}
            isActive={
              err.trim().length === 0 && errorCheck() === false ? true : false
            }
          >
            {loading ? "Loading..." : "CREATE"}
          </Button>
        </Form>
      </Wrapper>
    </Container>
  );
};

export default Register;
