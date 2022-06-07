<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Kits"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Título
            </th>
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
            <td>
              <a href="#/pages/product/kit">{{ item.title }}</a>
            </td>
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
            title: 'Kit para corte cabelo',
            description: 'Already sign employee international quality human.',
          },
          {
            title: 'Kit para maquiagem',
            description: 'Point who financial town head claim.',
          },
          {
            title: 'Kit para sobrancelha',
            description: 'See reflect put big least whom.',
          },
          {
            title: 'Kit para mão e pé',
            description: 'Eye student each conference term while must.',
          },
          {
            title: 'Kit para depilação',
            description: 'Order we receive hour bar.',
          },
        ],
      }
    },
  }
</script>
