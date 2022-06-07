<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Estoque Saída"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Código
            </th>
            <th class="primary--text">
              Criado por
            </th>
            <th class="primary--text">
              Criado em
            </th>
            <th class="primary--text">
              Status
            </th>
            <th class="text-right primary--text">
              Editar
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="item in items"
            :key="item"
          >
            <td>{{ item.slug }}</td>
            <td>{{ item.created_by }}</td>
            <td>{{ item.created }}</td>
            <td>{{ item.status }}</td>
            <td class="text-right">
              <v-icon class="mx-1">
                mdi-pencil
              </v-icon>
            </td>
          </tr>
        </tbody>
      </v-simple-table>
    </base-material-card>
  </v-container>
</template>

<script>
  export default {
    data () {
      return {
        items: [
          {
            slug: 'q12r14',
            created_by: 'John Stewart',
            created: '26/10/2020',
            status: 'confirmado',
          },
          {
            slug: 'ac12d5',
            created_by: 'John Stewart',
            created: '27/10/2020',
            status: 'pendente',
          },
          {
            slug: 'de14f9',
            created_by: 'John Stewart',
            created: '27/10/2020',
            status: 'finalizado',
          },
          {
            slug: 'a17d15',
            created_by: 'John Stewart',
            created: '28/10/2020',
            status: 'cancelado',
          },
          {
            slug: 'r2d2cc',
            created_by: 'John Stewart',
            created: '28/10/2020',
            status: 'finalizado',
          },
        ],
      }
    },
  }
</script>
