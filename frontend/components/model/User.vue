<script lang="ts" setup>
import { CompleteUser } from '@/prisma/zod';

const props = defineProps<{
  user: CompleteUser,
}>();

const showPosts = useState(`${props.user.id}-show-posts`, () => true);

const havePosts = computed(() => props.user.posts && props.user.posts.length > 0);
</script>

<template>
  <Card
    class="shadow"
    header-bg-color="bg-blue-500"
  >
    <template #header>
      <div class="flex text-blue-200 space-x-2 items-center">
        <span>{{ user.name }}</span>
        <span class="px-2 py-1 leading-none border border-blue-200 rounded-full">
          ID {{ user.id }}
        </span>
      </div>
    </template>
    <div>
      <div
        class="flex text-lg font-bold items-center space-x-1"
        role="button"
        :class="{
          'disabled cursor-default text-gray-400': !havePosts,
        }"
        @click.prevent="showPosts = !showPosts"
      >
        <span>
          Posts
        </span>
        <span
          v-if="havePosts"
          class="transition duration-500 transform"
          :class="{'rotate-x-180': showPosts}"
        >
          <i
            class="icon-chevron-up"
          />
        </span>
      </div>
      <div
        v-if="showPosts && havePosts"
        class="mt-2"
      >
        <ModelPost
          v-for="post in user.posts"
          :key="post.id"
          :post="post"
        />
      </div>
    </div>
  </Card>
</template>
