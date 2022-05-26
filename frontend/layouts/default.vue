<template>
  <div class="w-max py-8 mx-auto">
    <h1 class="py-2">
      <pre class="inline">python-nuxt Test</pre>
    </h1>
    <slot />
  </div>
</template>

<style>
.input-text {
  @apply "input[text] p-1 caret-blue-500 outline-0 border rounded focus:border-blue-500";
}

.text-area {
  @apply "input-text min-h-8.5 focus:border-blue-500"
}

.btn > button {
  @apply "text-white bg-gray-500 border-2 border-gray-500 rounded hover:(bg-gray-600 border-gray-600)";
}

.btn-blue > button {
  @apply "bg-blue-500 border-blue-500 hover:(bg-blue-600 border-blue-600)";
}

.btn-green > button {
  @apply "bg-green-500 border-green-500 hover:(bg-green-600 border-green-600)";
}
</style>
