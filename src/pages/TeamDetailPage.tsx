import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { toast } from 'react-toastify';
import DetailHeader from '../components/DetailHeader';
import StatCard from '../components/StatCard';
import './DetailPage.css';

const TeamDetailPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const { isLoggedIn, favorites, addFavorite, removeFavorite, getToken } = useAuth();

  // Estados para gerenciar os dados da API, carregamento e erros
  const [teamData, setTeamData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    // Função assíncrona para buscar os dados do time
    const fetchTeamData = async () => {
      setLoading(true);
      setError(null);

      try {
        const response = await fetch(`http://localhost:8000/api/teams/${id}/`);

        // Verifica se a resposta da API foi bem-sucedida
        if (!response.ok) {
          throw new Error(`Erro na API: ${response.statusText} (Status: ${response.status})`);
        }

        const data = await response.json();
        console.log(data)
        
        // Verifica se a resposta contém os dados esperados
        if (data.response && data.response.length > 0) {
          setTeamData(data.response[0]); // Salva o primeiro item do array de resposta
        } else {
          throw new Error("Time não encontrado na API.");
        }

      } catch (err) {
        // Captura e salva qualquer erro que ocorra durante a chamada
        setError(err.message);
        console.error("Falha ao buscar detalhes do time:", err);
      } finally {
        // Garante que o loading seja desativado ao final
        setLoading(false);
      }
    };

    fetchTeamData();
  }, [id, getToken]); // Dependências do useEffect

  // Renderização condicional com base nos estados
  if (loading) {
    return <div className="main-content"><h2>Carregando...</h2></div>;
  }

  if (error) {
    return <div className="main-content"><h2>Erro: {error}</h2></div>;
  }

  if (!teamData) {
    return <div className="main-content"><h2>Time não encontrado!</h2></div>;
  }

  // Extrai os dados do time e do estádio para facilitar o acesso
  const { team, venue } = teamData;

  const isFavorited = favorites.some(fav => fav.id === team.id && fav.type === 'team');

  const handleFavoriteClick = () => {
    // Monta o objeto a ser salvo nos favoritos
    const teamItem = { id: team.id, name: team.name, type: 'team', path: `/time/${team.id}` };
    if (isFavorited) {
      removeFavorite(teamItem);
      toast.info(`${team.name} removido dos favoritos.`);
    } else {
      addFavorite(teamItem);
      toast.success(`${team.name} adicionado aos favoritos.`);
    }
  };

  return (
    <div className="main-content">
      <img src={`https://media.api-sports.io/football/teams/${team.id}.png`} alt="" className='team-photo' />
      <DetailHeader name={team.name} logo={team.logo}>
        {isLoggedIn && (
          <button onClick={handleFavoriteClick} className="auth-button" style={{ width: 'auto' }}>
            {isFavorited ? 'Remover dos Favoritos' : 'Adicionar aos Favoritos'}
          </button>
        )}
      </DetailHeader>

      <div className="stats-grid">
        <StatCard title="País" value={team.country || 'N/A'} />
        <StatCard title="Fundado em" value={team.founded || 'N/A'} />
        <StatCard title="Estádio" value={venue.name || 'N/A'} />
        <StatCard title="Cidade do Estádio" value={venue.city || 'N/A'} />
      </div>

      <button onClick={() => navigate(-1)} className="back-link">
        ← Voltar
      </button>
    </div>
  );
};

export default TeamDetailPage;