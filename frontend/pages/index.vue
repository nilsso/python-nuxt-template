<script lang="ts" setup>
import { _UserPrisma } from '@/prisma/zod/user';

const { data, pending, refresh } = await useFetch<unknown[]>('http://localhost:8000/user/find/many', { server: false });

interface User {
  id?: number,
  name?: string,
}

const users = useState<User[] | null>('users', () => null);

const createUser = async () => {
  await $fetch('http://localhost:8000/user/create/next', {
    method: 'POST',
  });
  refresh();
};

const deleteRandomUser = async() => {
  await $fetch('http://localhost:8000/user/delete/random', { method: 'POST' });
  refresh();
};

const deleteAllUsers = async() => {
  await $fetch('http://localhost:8000/user/delete/all', { method: 'POST' });
  refresh();
};

watch(pending, () => users.value = data.value.map(d => _UserPrisma.parse(d)));
</script>

<template>
  <div>
    <h2>Index</h2>
    <div>
      <h3>Users</h3>
      <div>
        <button
          class="px-1 py-.5 text-white bg-blue-500 border-2 border-blue-500 rounded"
          role="button"
          @click.prevent="createUser"
        >
          Create Next
        </button>
      </div>
      <div>
        <button
          class="px-1 py-.5 text-red-500 bg-white border-2 border-red-500 rounded"
          role="button"
          @click.prevent="deleteRandomUser"
        >
          Delete Random
        </button>
        <button
          class="px-1 py-.5 text-white bg-red-500 border-2 border-red-500 rounded"
          role="button"
          @click.prevent="deleteAllUsers"
        >
          Delete All
        </button>
      </div>
      <p v-if="users === null">
        Waiting...
      </p>
      <div v-else>
        <div
          v-for="user in users"
          :key="user.id"
        >
          <span>
            ID: {{ user.id }}
          </span>
          <span>
            Name: {{ user.name }}
          </span>
        </div>
      </div>
    </div>
  </div>
</template>
