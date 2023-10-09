<template>
  <div class="content-block">
    <div class="title">{{ title }}</div>
    <div class="content-wrapper">
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
      <div class="card"></div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    title: {
      type: String,
      require: true,
    },
  },
};
</script>

<style lang="scss" scoped>
.content-block {
  padding: 0 30px 30px;
  .title {
    color: rgb(255, 255, 255);
    font-size: 1.5rem;
    font-weight: 100;
    margin-bottom: 0.5rem;
  }
  .content-wrapper {
    width: 100%;
    height: 150px;
    display: flex;
    overflow: hidden;
    gap: 10px;
    .card {
      flex: none;
      width: 220px;
      height: 100%;
      background-color: #fff;
    }
  }
}
</style>
