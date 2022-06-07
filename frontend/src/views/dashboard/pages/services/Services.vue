<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Serviços"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Descrição
            </th>
            <th class="primary--text">
              Preço
            </th>
            <th class="primary--text">
              Comissão
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
              <a href="#/pages/services/service">{{ item.description }}</a>
            </td>
            <td>R$ <span class="">{{ item.value }}</span></td>
            <td>{{ item.comission }}%</td>
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
            description: 'Corte cabelo',
            value: 45.15,
            comission: 30,
          },
          {
            description: 'Maquiagem',
            value: 39.99,
            comission: 30,
          },
          {
            description: 'Sobrancelha',
            value: 65.19,
            comission: 30,
          },
          {
            description: 'Mão e Pé',
            value: 90.09,
            comission: 30,
          },
          {
            description: 'Depilação',
            value: 120.99,
            comission: 30,
          },
        ],
      }
    },
  }
</script>
