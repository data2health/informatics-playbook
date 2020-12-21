<template>
  <li>
    <span>{{ todo.text }}</span>
    <button @click.prevent="$emit('remove', todo)">Remove</button>
  </li>
</template>

<script>
export default {
  props: {
    todo: {
      required: true,
      type: Object
    }
  }
}
</script>


<style scoped>

</style>