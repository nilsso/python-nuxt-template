<script lang="ts" setup>
import { UserPrisma, CompleteUser } from '@/prisma/zod/user';

const { data, pending, refresh } = await useFetch<unknown[]>(
  'http://localhost:8000/user',
  {
    server: false,
    method: 'POST',
    headers: {
      'Accept': 'application/json',
      'Content-Type': 'application/json',
    },
    body: {
      // take: 1,
      // skip: 0,
      include: {
        posts: true,
      },
    },
  },
);

const users = useState<CompleteUser[] | null>('users', () => null);

watch(pending, () => {
  const parsed = data.value.map(d => UserPrisma.parse(d));
  console.dir(parsed);
  users.value = parsed;
});

// const createUser = async () => {
//   await $fetch('http://localhost:8000/user/next', { method: 'POST' });
//   refresh();
// };
//
// const deleteRandomUser = async() => {
//   await $fetch('http://localhost:8000/user/random', { method: 'DELETE' });
//   refresh();
// };
//
// const deleteAllUsers = async() => {
//   await $fetch('http://localhost:8000/user/all', { method: 'DELETE' });
//   refresh();
// };
</script>

<template>
  <div class="space-y-2">
    <Card
      class="w-max shadow"
      header-bg-color="bg-cyan-500"
    >
      <template #header>
        <div class="flex space-x-2">
          <div class="text-cyan-200">
            <span>Users</span>
          </div>
          <!-- <button -->
          <!--   class="inline block p-0 text-sm leading-0 text-white bg-blue-500 border-2 border-blue-500 rounded" -->
          <!--   role="button" -->
          <!-- > -->
          <!--   Create Next -->
          <!-- </button> -->
          <!-- <button -->
          <!--   class="px-1 py-.5 text-base text-red-500 bg-white border-2 border-red-500 rounded" -->
          <!--   role="button" -->
          <!-- > -->
          <!--   Delete Random -->
          <!-- </button> -->
          <!-- <button -->
          <!--   class="px-1 py-.5 text-base text-white bg-red-500 border-2 border-red-500 rounded" -->
          <!--   role="button" -->
          <!-- > -->
          <!--   Delete All -->
          <!-- </button> -->
        </div>
      </template>
      <p v-if="users === null">
        Waiting...
      </p>
      <div
        v-else
        class="flex flex-col space-y-2"
      >
        <ModelUser
          v-for="user in users"
          :key="user.id"
          :user="user"
        />
      </div>
    </Card>
  </div>
</template>
