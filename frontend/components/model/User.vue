<script lang="ts" setup>
import { CompleteUser } from '@/prisma/zod';
import { modelRequest } from '@/common';

const props = defineProps<{
  user: CompleteUser,
}>();

const emit = defineEmits<{
  (e: 'delete', id: number): void,
  (e: 'refresh'): void,
}>();

const showPosts = useState(`user-${props.user.id}-show-posts`, () => true);
const createPostShow = useState(`user-${props.user.id}-create-post-show`, () => false);
const createPostTitle = useState(`user-${props.user.id}-create-post-name`, () => '');

const havePosts = computed(() => props.user.posts && props.user.posts.length > 0);
</script>

<template>
  <Card
    class="shadow"
    header-bg-color="bg-blue-500"
  >
    <template #header>
      <div class="flex text-blue-200 space-x-2 items-center">
        <div class="flex space-x-2 items-center">
          <span>{{ user.name }}</span>
          <span class="px-2 py-1 leading-none border border-blue-200 rounded-full">
            ID {{ user.id }}
          </span>
        </div>
        <span class="flex-1" />
        <div
          role="button"
          class="transition hover:text-red-300"
          @click.prevent="emit('delete', user.id)"
        >
          <i class="icon-close-o" />
        </div>
      </div>
    </template>
    <div>
      <div
        class="flex text-lg font-bold items-center"
      >
        <div
          role="button"
          class="flex items-center space-x-1"
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
        <span class="flex-1" />
        <div
          role="button"
          class="text-gray-400 transition hover:text-green-500"
          @click.prevent="createPostShow = true"
        >
          <i class="icon-add" />
        </div>
      </div>
      <div>
        <Card
          v-show="createPostShow"
          class="mt-2"
        >
          <template #header>
            <div class="flex items-center">
              <div>Create New Post</div>
              <span class="flex-1" />
              <div
                role="button"
                class="transition hover:text-red-300"
                @click.prevent="createPostShow = false"
              >
                <i class="icon-close-o" />
              </div>
            </div>
          </template>
          <form class="flex flex-col space-y-2">
            <input
              v-model="createPostTitle"
              type="text"
              class="w-full input-text"
              placeholder="Title"
            >
            <textarea
              class="w-full text-area"
              placeholder="Content"
            />
            <div class="flex flex-row-reverse">
              <div class="relative btn btn-green">
                <button
                  class="px-2 py-.5"
                  :disabled="createPostTitle === ''"
                  @click.prevent="modelRequest('post', 'create', 'PUT', {
                    data: {
                      title: createPostTitle,
                      user: {
                        connect: {
                          id: user.id,
                        },
                      },
                    },
                  }).then(() => {
                    emit('refresh');
                    createPostShow = false;
                  })"
                >
                  Create
                </button>
                <div
                  v-show="createPostTitle.length === 0"
                  class="absolute inset-0 bg-gray-500 bg-opacity-30 rounded"
                />
              </div>
            </div>
          </form>
        </Card>
        <div
          v-show="showPosts && havePosts"
          class="contents"
        >
          <ModelPost
            v-for="post in user.posts"
            :key="post.id"
            :post="post"
            class="mt-2"
            @delete="(id: number) => modelRequest('post', 'delete', 'DELETE', {
              where: {
                id,
              }
            }).then(() => emit('refresh'))"
            @refresh="emit('refresh')"
          />
        </div>
      </div>
    </div>
  </Card>
</template>
