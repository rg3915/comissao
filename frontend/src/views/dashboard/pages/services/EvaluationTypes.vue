<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Tipos de Avaliações"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Descrição
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
            <td>{{ item.description }}</td>
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
            description: 'Está de rimel',
          },
          {
            description: 'Alergia a esmalte ou cosméticos',
          },
          {
            description: 'Problemas de tireóide',
          },
          {
            description: 'Algum procedimento feito recentemente nos olhos',
          },
          {
            description: 'Glaucoma/blefarite/algum problema ocular',
          },
          {
            description: 'Grávida',
          },
          {
            description: 'Tratamento oncológico',
          },
        ],
      }
    },
  }
</script>
