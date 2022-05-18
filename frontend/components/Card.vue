<script lang="ts" setup>
const props = defineProps<{
  headerColor?: string,
  headerBgColor?: string,
}>();

const headerColor = props.headerColor || 'text-gray-200';
const headerBgColor = props.headerBgColor || 'bg-gray-500';
</script>
<template>
  <div class="rounded-lg">
    <div
      v-if="!!$slots.header"
      class="rounded-t-lg"
      :class="`text-sm ${headerBgColor}`"
    >
      <div
        class="my-0 mx-2 leading-loose text-xl font-sans"
        :class="headerColor"
      >
        <slot name="header" />
      </div>
    </div>
    <div
      :class="!$slots.header ? 'border rounded-lg' : 'border-b border-x rounded-b-lg'"
    >
      <div
        class="p-2 bg-white rounded-lg"
        :class="!$slots.header ? 'rounded-lg' : 'rounded-b-lg'"
      >
        <slot name="default" />
      </div>
    </div>
  </div>
</template>
