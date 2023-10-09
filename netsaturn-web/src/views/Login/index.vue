<template>
  <div class="login">
    <h1 class="logo">神马视频</h1>
    <div class="login-card">
      <div class="title">登入</div>
      <form>
        <input type="text" placeholder="邮箱" />
        <input type="text" placeholder="密码" />
        <button>登入</button>
      </form>
      <div class="footer">
        <a href="">忘记密码</a>
        <p>没有账号？<a href="">立即注册</a></p>
      </div>
    </div>
  </div>
</template>

<script>
import { reactive, toRefs } from "vue";

export default {
  setup() {
    const state = reactive({
      count: 0,
    });

    return {
      ...toRefs(state),
    };
  },
};
</script>

<style lang="scss" scoped>
@import "@/styles/common.scss";

.login {
  width: 100vw;
  height: 100vh;
  background-image: url("./images/bg.jpg");
  padding: 0 15px;
  position: relative;
  &::before {
    content: "";
    display: block;
    position: absolute;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    left: 0;
    top: 0;
  }

  .logo {
    position: relative;
    font-size: 50px;
    font-weight: bold;
    height: 100px;
    line-height: 100px;
    padding: 0 20px;
    color: rgb(224, 0, 32);
    margin-bottom: 30px;
  }

  .login-card {
    position: relative;
    width: min(460px, 100%);
    margin: auto;
    background-color: rgba(0, 0, 0, 0.7);
    padding: 4rem;
    @include borderRadius;
    .title {
      font-size: 32px;
      color: rgb(255, 255, 255);
      margin-bottom: 20px;
      font-weight: 100;
    }
    form {
      margin-bottom: 1rem;
      input {
        display: block;
        background-color: rgba(51, 51, 51);
        width: 100%;
        height: 3rem;
        margin-bottom: 2rem;
        border: 0;
        outline: none;
        color: rgb(255, 255, 255);
        padding: 0 10px;
        @include borderRadius;
        &:focus {
          background-color: rgb(69, 69, 69);
        }
        &::placeholder {
          color: rgb(200, 200, 200);
        }
      }
      button {
        width: 100%;
        height: 3.5rem;
        color: rgb(255, 2552, 255);
        background-color: rgb(224, 0, 32);
        @include borderRadius;
      }
    }

    .footer {
      color: rgb(160, 160, 160);
      display: flex;
      justify-content: space-between;
      a {
        color: rgb(220, 220, 220);
      }
    }
  }
}
</style>
