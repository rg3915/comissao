<template>
  <v-container
    id="regular-tables"
    fluid
    tag="section"
  >
    <base-material-card
      icon="mdi-clipboard-text"
      title="Tipos de Despesas"
      class="px-5 py-3"
    >
      <v-simple-table>
        <thead>
          <tr>
            <th class="primary--text">
              Tipo de Despesa
            </th>
            <th class="primary--text">
              Categoria
            </th>
            <th class="primary--text">
              Fixa
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
            <td>{{ item.type_expense }}</td>
            <td>{{ item.category_expense }}</td>
            <td v-if="item.fixed">
              <v-icon
                class="mx-1"
                style="color: green"
              >
                mdi-check
              </v-icon>
            </td>
            <td v-else>
              <v-icon
                class="mx-1"
                style="color: red"
              >
                mdi-close
              </v-icon>
            </td>
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
            type_expense: 'Aluguel',
            category_expense: 'Imóvel',
            fixed: true,
          },
          {
            type_expense: 'Celular',
            category_expense: 'Comunicação',
            fixed: true,
          },
          {
            type_expense: 'Combustível',
            category_expense: 'Transporte',
            fixed: false,
          },
          {
            type_expense: 'Comissão',
            category_expense: 'Funcionário',
            fixed: false,
          },
          {
            type_expense: 'Diversos',
            category_expense: 'Diversos',
            fixed: false,
          },
          {
            type_expense: 'Funcionário',
            category_expense: 'Funcionário',
            fixed: true,
          },
          {
            type_expense: 'Internet',
            category_expense: 'Consumo',
            fixed: true,
          },
          {
            type_expense: 'Luz',
            category_expense: 'Consumo',
            fixed: true,
          },
          {
            type_expense: 'Produto',
            category_expense: 'Matéria',
            fixed: false,
          },
          {
            type_expense: 'Seguro',
            category_expense: 'Seguro',
            fixed: true,
          },
          {
            type_expense: 'Telefone',
            category_expense: 'Comunicação',
            fixed: true,
          },
          {
            type_expense: 'Água',
            category_expense: 'Consumo',
            fixed: true,
          },
        ],
      }
    },
  }
</script>
