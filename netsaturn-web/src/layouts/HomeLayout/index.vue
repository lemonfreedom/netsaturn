<template>
  <div>
    <Header />
    <router-view />
  </div>
</template>

<script>
import Header from "@/components/Header/index.vue";
export default {
  components: { Header },
};
</script>

<style lang="scss" scoped>
</style>
