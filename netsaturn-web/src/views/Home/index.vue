<template>
  <div class="home">
    <div
      class="banner"
      :style="{
        '--banner-url': `url(${bannerUrl})`,
      }"
    >
      <div class="info">
        <div class="title">飙速求生</div>
        <div class="action">
          <button>播放</button>
          <button class="more">更多资讯</button>
        </div>
      </div>
    </div>

    <ContentBlock title="热播电影" />
    <ContentBlock title="热播电视剧" />
  </div>
</template>

<script>
import bannerUrl from "./images/1.webp";
import ContentBlock from "@/components/ContentBlock/index.vue";
export default {
  components: { ContentBlock },
  data() {
    return {
      bannerUrl,
    };
  },
};
</script>

<style lang="scss" scoped>
@import "@/styles/common.scss";
.home {
  .banner {
    height: 600px;
    background: var(--banner-url) no-repeat center;
    background-size: cover;
    position: relative;
    margin-bottom: 30px;
    .info {
      position: absolute;
      bottom: 60px;
      left: 60px;
      .title {
        font-size: 40px;
        font-weight: 100;
        color: rgb(255, 255, 255);
        text-shadow: 1px 1px 1px rgb(0, 0, 0);
        margin-bottom: 20px;
        letter-spacing: 0.3rem;
      }
      .action {
        display: flex;
        gap: 20px;
        button {
          background-color: rgb(255, 255, 255);
          padding: 8px 15px;
          @include borderRadius(0.2rem);
          cursor: pointer;

          &.more {
            color: rgb(255, 255, 255);
            background-color: rgb(98, 95, 89, 0.6);
          }
        }
      }
    }
  }
}
</style>
