<script lang="ts" setup>
import { Ref } from 'vue';
import { UserPrisma, CompleteUser } from '@/prisma/zod/user';
import { modelRequest } from '@/common';

const {
  data: usersData,
  pending: usersPending,
  refresh: usersRefresh,
} = await useFetch<unknown[]>(
  'http://localhost:8000/user/find_many',
  {
    server: false,
    method: 'POST',
    body: {
      include: {
        posts: {
          include: {
            tags: true,
          },
        },
      },
    },
  },
);

const users = useState<CompleteUser[] | null>('users', () => null);
const createUserShow = useState('show-create', () => false);
const createUserName = useState('create-name', () => '');

watch(usersPending, () => {
  users.value = usersData.value.map(d => UserPrisma.parse(d));
});

const fileInput: Ref<HTMLInputElement | null> = ref(null);
const uploadFile = useState<File | null>('upload-file', () => null);

function eventFiles(e: Event): FileList {
  const target = e.target as HTMLInputElement | null;
  const files = target?.files;
  if (!(files?.length > 0)) {
    throw 'event did not have files';
  }
  return files;
}

function eventFile(e: Event): File {
  const files = eventFiles(e);
  if (!(files.length === 1)) {
    throw 'event had more than one file';
  }
  return files[0];
}

watch(uploadFile, () => console.dir(uploadFile.value));

function clearFile() {
  if (fileInput.value) {
    fileInput.value.value = '';
    uploadFile.value = null;
  }
}
</script>

<template>
  <div class="space-y-2">
    <div class="space-x-2">
      <button
        class="btn"
        :disabled="uploadFile === null"
        @click.prevent=""
      >
        Upload
      </button>
      <input
        ref="fileInput"
        type="file"
        @change="(e) => uploadFile = eventFile(e)"
      >
      <button
        class="btn btn-red"
        @click.prevent="clearFile"
      >
        Clear
      </button>
      <span>{{ fileInput?.value }}</span>
    </div>
    <Card
      class="w-100 shadow"
      header-bg-color="bg-cyan-500"
    >
      <template #header>
        <div class="flex space-x-2 items-center text-cyan-200">
          <div>Users</div>
          <span class="flex-1" />
          <div
            role="button"
            class="transition hover:text-green-300"
            @click.prevent="createUserShow = true"
          >
            <i class="icon-add" />
          </div>
        </div>
      </template>
      <p v-if="users === null">
        Waiting...
      </p>
      <div
        v-else
        class="flex flex-col space-y-2"
      >
        <Card v-show="createUserShow">
          <template #header>
            <div class="flex items-center">
              <div>Create New User</div>
              <span class="flex-1" />
              <div
                role="button"
                class="transition hover:text-red-300"
                @click.prevent="createUserShow = false"
              >
                <i class="icon-close-o" />
              </div>
            </div>
          </template>
          <form
            class="flex flex-col space-y-2"
            @submit.prevent="modelRequest('user', 'create', 'PUT', {
              data: {
                name: createUserName,
              },
            }).then(() => usersRefresh().then(() => createUserShow = false))"
          >
            <div>
              <input
                v-model="createUserName"
                type="text"
                class="w-full input-text"
                placeholder="Name"
              >
            </div>
            <div class="flex flex-row-reverse">
              <div class="relative btn btn-green">
                <button
                  class="px-2 py-.5"
                  type="submit"
                  :disabled="createUserName === ''"
                >
                  Create
                </button>
                <div
                  v-show="createUserName.length === 0"
                  class="absolute inset-0 bg-gray-500 bg-opacity-30 rounded"
                />
              </div>
            </div>
          </form>
        </Card>
        <ModelUser
          v-for="user in users"
          :key="user.id"
          :user="user"
          @refresh="usersRefresh()"
          @delete="(id: number) => modelRequest('user', 'delete', 'DELETE', {
            where: {
              id,
            }
          }).then(() => usersRefresh())"
        />
      </div>
    </Card>
  </div>
</template>

<style scoped>
.btn {
  @apply "px-2 text-white border-2 rounded";
}

.btn:not(:disabled) {
  @apply "bg-blue-500 border-blue-500 hover:(bg-blue-600 border-blue-600) active:(bg-blue-700 border-blue-700)";
}

.btn:disabled {
  @apply "bg-blue-700 border-blue-700 cursor-default opacity-50";
}
</style>
