<template>
  <div ref="header" class="header">
    <div>
      <div class="logo">神马视频</div>
      <ul>
        <li><a href="">首页</a></li>
        <li><a href="">电影</a></li>
        <li><a href="">电视剧</a></li>
        <li><a href="">最新热门影片</a></li>
        <li><a href="">我的收藏</a></li>
      </ul>
    </div>
    <div>
      <ul>
        <li>
          <a href="">
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="20"
              height="20"
              fill="currentColor"
              viewBox="0 0 16 16"
            >
              <path
                d="M11.742 10.344a6.5 6.5 0 1 0-1.397 1.398h-.001c.03.04.062.078.098.115l3.85 3.85a1 1 0 0 0 1.415-1.414l-3.85-3.85a1.007 1.007 0 0 0-.115-.1zM12 6.5a5.5 5.5 0 1 1-11 0 5.5 5.5 0 0 1 11 0z"
              />
            </svg>
          </a>
        </li>
        <li>
          <a href="">
            <div
              :style="{
                '--avatar-url': `url(${avatarUrl})`,
              }"
              class="avatar"
            ></div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="12"
              height="12"
              fill="currentColor"
              viewBox="0 0 16 16"
            >
              <path
                d="M7.247 11.14 2.451 5.658C1.885 5.013 2.345 4 3.204 4h9.592a1 1 0 0 1 .753 1.659l-4.796 5.48a1 1 0 0 1-1.506 0z"
              />
            </svg>
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import Headroom from "headroom.js";
import avatarUrl from "./images/1.png";
export default {
  data() {
    return {
      avatarUrl,
    };
  },
  mounted() {
    new Headroom(this.$refs.header).init();
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
@import "@/styles/common.scss";
.header {
  justify-content: space-between;
  color: rgb(255, 255, 255);
  background-color: rgb(0, 0, 0, 0.8);
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  display: flex;
  height: 68px;
  line-height: 68px;
  padding: 0 20px;
  z-index: 999;
  > div {
    display: flex;
    .logo {
      font-size: 20px;
      padding: 0 10px;
      margin-right: 10px;
      font-weight: bold;
      color: rgb(224, 0, 32);
    }
    ul {
      display: flex;
      align-items: center;
      li {
        padding: 0 10px;
        a {
          display: flex;
          align-items: center;
          &:hover {
            color: rgb(220, 220, 220);
          }
        }
      }
    }
  }

  .avatar {
    width: 30px;
    height: 30px;
    @include borderRadius();
    background: var(--avatar-url) no-repeat center;
    background-size: cover;
    margin-right: 6px;
  }

  &.headroom {
    will-change: transform;
    transition: transform 200ms linear;
  }
  &.headroom--pinned {
    transform: translateY(0%);
  }
  &.headroom--unpinned {
    transform: translateY(-100%);
  }
}
</style>
