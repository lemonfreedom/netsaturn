<template>
  <div>
    <button @click="jx">解析</button>
    <iframe width="800px" height="500px" src="https://jx.m3u8.tv/jiexi/?url=https://v.qq.com/x/cover/mzc002006w8m6hk/o0047hfgj2t.html" frameborder="0"></iframe>
  </div>
</template>

<script>
export default {
  created() {

  },
  methods: {
    jx() {
      fetch('https://jx.m3u8.tv/jiexi/?url=https://v.qq.com/x/cover/mzc002006w8m6hk/o0047hfgj2t.html').then(res => {
        console.log(res);
      })

    }
  }
}
</script>

<style lang="scss" scoped></style>
