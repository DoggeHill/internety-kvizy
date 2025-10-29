import React, {useState} from 'react';
import Card from '../components/core/UI/Card.react';
import Text from '../components/core/UI/Text.react';
import VerticalLayout from '../components/core/layout/VerticalLayout.react';
import QuestionList from './components/QuestionList.react';
import Button from '../components/core/UI/Button.react';
import {getStringHash} from '../service/util/util';
import Header from '../components/core/UI/Header.react';
import Sidebar from '../components/core/UI/Sidebar.react';
import Modal from '../components/core/UI/Modal.react';
import classes from './Quiz.module.css';
import Timer from '../components/core/UI/Timer.react';
import ProgressRing from './components/QuizProgress.react';
import QuizScore from './components/QuizScore.react';
// import IconWrapper from '../components/core/UI/IconWrapper.react';
import QuizEnd from './QuizEnd.react';

const getTimerHash = () => `timer_${getStringHash('timer', Date.now())}`;

const Quiz = ({data, setData, finishQuiz, restartQuiz, onSaveIncorrectAnswers, onRemoveCorrectAnswers, isRetryQuiz}) => {
  const [timerKey, setTimerKey] = useState(getTimerHash());
  const [answer, setAnswer] = useState(null);
  const [quizEnd, setQuizEnd] = useState(false);
  const [questionIndex, setQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [answered, setAnswered] = useState(0);
  const [incorrectAnswers, setIncorrectAnswers] = useState([]);
  const [correctAnswersInRetry, setCorrectAnswersInRetry] = useState([]);
  const [userAnswers, setUserAnswers] = useState([]);
  const [showIncorrectAnswers, setShowIncorrectAnswers] = useState(false);
  const {question, options, correct, explanation, multipleCorrect} = data[questionIndex];
  const [selectedAnswers, setSelectedAnswers] = useState([]);
  
  // Store original quiz state before switching to incorrect answers
  const [savedQuizState, setSavedQuizState] = useState(null);

  const answerHandler = (isCorrect, selectedOption) => {
    if (isCorrect) {
      // Correct answer logic
      setScore(prevScore => prevScore + 1);
      
      // If this is a retry quiz, track correctly answered questions
      if (isRetryQuiz) {
        setCorrectAnswersInRetry(prev => [...prev, question]);
      }
    } else {
      setIncorrectAnswers(incorrect => [
        ...incorrect,
        {
          question,
          options,
          correct,
          explanation,
          userAnswer: multipleCorrect ? selectedAnswers : selectedOption,
          questionIndex,
          multipleCorrect,
        },
      ]);
    }
    setAnswered(prevAnswered => prevAnswered + 1);
  };

  const quizRestartHandler = () => {
    setQuizEnd(false);
    setIncorrectAnswers([]);
    setCorrectAnswersInRetry([]);
    setAnswer(null);
    setSelectedAnswers([]);
    setQuestionIndex(0);
    setScore(0);
    setAnswered(0);
    resetTimer();
    restartQuiz();
  };

  const resetTimer = () => {
    setTimerKey(getTimerHash());
  };

  const startIncorrectAnswersSession = () => {
    if (incorrectAnswers.length > 0) {
      // Save current quiz state so we can return to it later
      setSavedQuizState({
        data: data,
        questionIndex: questionIndex,
        score: score,
        answered: answered,
        incorrectAnswers: incorrectAnswers,
        timerKey: timerKey,
      });
      
      // Save current incorrect answers to localStorage
      if (onSaveIncorrectAnswers) {
        onSaveIncorrectAnswers(incorrectAnswers);
      }
      
      // Create new quiz data from incorrect answers
      const incorrectQuestionsData = incorrectAnswers.map(item => ({
        question: item.question,
        options: item.options,
        correct: item.correct,
        explanation: item.explanation,
        multipleCorrect: item.multipleCorrect,
      }));
      
      // Reset quiz state and start with incorrect questions
      setData(incorrectQuestionsData);
      setQuizEnd(false);
      setIncorrectAnswers([]);
      setCorrectAnswersInRetry([]);
      setAnswer(null);
      setSelectedAnswers([]);
      setQuestionIndex(0);
      setScore(0);
      setAnswered(0);
      resetTimer();
    }
  };

  const continueOriginalQuiz = () => {
    if (savedQuizState) {
      // Restore the original quiz state
      setData(savedQuizState.data);
      setQuestionIndex(savedQuizState.questionIndex);
      setScore(savedQuizState.score);
      setAnswered(savedQuizState.answered);
      setIncorrectAnswers(savedQuizState.incorrectAnswers);
      setTimerKey(savedQuizState.timerKey);
      setQuizEnd(false);
      setAnswer(null);
      setSelectedAnswers([]);
      setSavedQuizState(null);
    }
  };

  return (
    <div className={classes.Quiz}>
      <Header text="JSON flashcards">
        <div className={classes.QuitButton}>
          <Button type="link" value="quit" onClick={finishQuiz} />
        </div>
      </Header>
      <div className={classes.QuizPanel}>
        <Sidebar>
          <div className={classes.Sidebar_Layout}>
            <VerticalLayout center="horizontal" spaceBetween={1.5}>
              <Text type="header2" bold>
                Stats
              </Text>
              <Timer key={timerKey} stop={answer || quizEnd ? true : false} />
              <ProgressRing current={questionIndex + 1} total={data.length} />
              <QuizScore current={score} total={answered} />
              {savedQuizState && (
                <div className={classes.ContinueQuizButton}>
                  <Button
                    type="button"
                    value="Continue Original Quiz"
                    onClick={continueOriginalQuiz}
                  />
                </div>
              )}
              {incorrectAnswers.length > 0 && !savedQuizState && (
                <>
                  <div className={classes.IncorrectAnswersButton}>
                    <Button
                      type="button"
                      value={`View Incorrect (${incorrectAnswers.length})`}
                      onClick={() => setShowIncorrectAnswers(true)}
                    />
                  </div>
                  <div className={classes.RetryIncorrectButton}>
                    <Button
                      type="button"
                      value={`Start New Session (${incorrectAnswers.length})`}
                      onClick={startIncorrectAnswersSession}
                    />
                  </div>
                </>
              )}
            </VerticalLayout>
            {/* <div className={classes.SettingsButton}>
              <IconWrapper iconType="gear" iconSize={1.5}>
                <div className={classes.SettingsButtonText}>
                  <Button type="link" value="settings"></Button>
                </div>
              </IconWrapper>
            </div> */}
          </div>
        </Sidebar>
        <VerticalLayout center="middle">
          {!quizEnd ? (
            <Card rounded>
              <div className={classes.QuestionWrapper}>
                <div className={classes.title}>
                  <Text type="header2" variant="primary" bold>
                    {question}
                  </Text>
                </div>
                <QuestionList
                  questionId={`question_${getStringHash(question)}`}
                  questions={options}
                  correct={correct}
                  shuffle={true}
                  showFeedback={answer ? true : false}
                  multipleCorrect={multipleCorrect}
                  selectedAnswers={selectedAnswers}
                  onAnswer={(option, isCorrect, optionIndex) => {
                    if (multipleCorrect) {
                      // Handle multiple selection
                      if (selectedAnswers.includes(optionIndex)) {
                        setSelectedAnswers(selectedAnswers.filter(i => i !== optionIndex));
                      } else {
                        setSelectedAnswers([...selectedAnswers, optionIndex]);
                      }
                    } else {
                      setAnswer(option);
                      answerHandler(isCorrect, optionIndex);
                    }
                  }}
                />
                {multipleCorrect && !answer && (
                  <div className={classes.SubmitButton}>
                    <Button
                      value="Submit Answer"
                      onClick={() => {
                        // Check if all correct answers are selected
                        const correctAnswers = Array.isArray(correct) ? correct : [correct];
                        const isCorrect = 
                          selectedAnswers.length === correctAnswers.length &&
                          selectedAnswers.every(ans => correctAnswers.includes(ans)) &&
                          correctAnswers.every(ans => selectedAnswers.includes(ans));
                        
                        setAnswer(selectedAnswers);
                        answerHandler(isCorrect, selectedAnswers);
                      }}
                      disabled={selectedAnswers.length === 0}
                    />
                  </div>
                )}
                {answer && explanation && (
                  <div className={classes.ExplanationBox}>
                    <Text type="body2" bold>
                      Explanation:
                    </Text>
                    <Text type="body2">{explanation}</Text>
                  </div>
                )}
                <div className={classes.TransitionButton}>
                  {questionIndex + 1 !== data.length ? (
                    <Button
                      hidden={!answer ? true : false}
                      value="Next"
                      onClick={() => {
                        setQuestionIndex(i => i + 1);
                        setAnswer(null);
                        setSelectedAnswers([]);
                      }}
                    />
                  ) : (
                    <Button
                      hidden={!answer ? true : false}
                      value="Finish"
                      onClick={() => {
                        setQuizEnd(true);
                        if (onSaveIncorrectAnswers && incorrectAnswers.length > 0) {
                          onSaveIncorrectAnswers(incorrectAnswers);
                        }
                        // If this is a retry quiz, remove correctly answered questions from the bank
                        if (isRetryQuiz && onRemoveCorrectAnswers && correctAnswersInRetry.length > 0) {
                          onRemoveCorrectAnswers(correctAnswersInRetry);
                        }
                      }}
                    ></Button>
                  )}
                </div>
              </div>
            </Card>
          ) : (
            <QuizEnd
              returnHome={finishQuiz}
              restartQuiz={quizRestartHandler}
              restartQuizIncorrect={() => {
                setData(incorrectAnswers);
                quizRestartHandler();
              }}
              hasIncorrectAnswers={incorrectAnswers.length > 0}
            />
          )}
        </VerticalLayout>
      </div>
      {showIncorrectAnswers && (
        <Modal show={showIncorrectAnswers} handleClose={() => setShowIncorrectAnswers(false)}>
          <Card>
            <div className={classes.IncorrectAnswersModal}>
              <VerticalLayout center="horizontal" spaceBetween={1}>
                <Text type="header2" bold>
                  Incorrect Answers ({incorrectAnswers.length})
                </Text>
                <div className={classes.IncorrectAnswersList}>
                  {incorrectAnswers.map((item, idx) => {
                    const correctAnswers = Array.isArray(item.correct) 
                      ? item.correct 
                      : [item.correct];
                    const userAnswers = Array.isArray(item.userAnswer)
                      ? item.userAnswer
                      : [item.userAnswer];
                    
                    return (
                      <div key={idx} className={classes.IncorrectAnswerItem}>
                        <Text type="body1" bold>
                          Q{item.questionIndex + 1}: {item.question}
                        </Text>
                        <div className={classes.AnswerDetails}>
                          <Text type="body2">
                            <strong>Your answer:</strong>{' '}
                            {userAnswers.map(ans => item.options[ans]).join(', ')}
                          </Text>
                          <Text type="body2">
                            <strong>Correct answer:</strong>{' '}
                            {correctAnswers.map(ans => item.options[ans]).join(', ')}
                          </Text>
                          {item.explanation && (
                            <Text type="body2">
                              <strong>Explanation:</strong> {item.explanation}
                            </Text>
                          )}
                        </div>
                      </div>
                    );
                  })}
                </div>
                <Button
                  type="button"
                  value="Close"
                  onClick={() => setShowIncorrectAnswers(false)}
                />
              </VerticalLayout>
            </div>
          </Card>
        </Modal>
      )}
    </div>
  );
};

export default Quiz;
