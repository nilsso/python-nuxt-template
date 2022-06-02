export default defineEventHandler(async (event) => {
  const { files } = await useBody(event);

  return {
    file: 'works',
  };
});
